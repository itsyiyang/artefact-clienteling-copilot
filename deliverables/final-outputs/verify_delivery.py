"""Validate the archived XLSX using Python's standard library (no dependencies)."""
from pathlib import Path
import collections
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile

FILE = Path(__file__).with_name('LIUXU_test_results_50_FINAL.xlsx')
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
HEADERS = ['Case ID', 'Scenario', 'Client Information', 'Conversation history',
           'Product information', 'Output 1', 'Output 2', 'Output 3']


def main():
    with zipfile.ZipFile(FILE) as archive:
        assert archive.testzip() is None, 'Damaged XLSX archive'
        strings = [''.join(n.itertext()) for n in
                   ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('s:si', NS)]
        workbook = ET.fromstring(archive.read('xl/workbook.xml'))
        assert [s.get('name') for s in workbook.findall('s:sheets/s:sheet', NS)] == [
            '案例与自然话术', '原始数据核对']
        sheets = []
        for index in (1, 2):
            sheet = ET.fromstring(archive.read(f'xl/worksheets/sheet{index}.xml'))
            assert len(sheet.findall('s:sheetData/s:row', NS)) == 51
            values = {}
            for cell in sheet.findall('.//s:sheetData/s:row/s:c', NS):
                assert cell.get('t') != 'e', cell.get('r')
                value = cell.find('s:v', NS)
                if value is not None:
                    values[cell.get('r')] = (strings[int(value.text)]
                                            if cell.get('t') == 's' else value.text)
            assert [values[f'{col}1'] for col in 'ABCDEFGH'] == HEADERS
            sheets.append(values)
    readable, original = sheets
    source = json.loads(FILE.with_name('source-data.json').read_text())
    assert source == [[original[f'{col}{row}'] for col in 'ABCDEFGH']
                      for row in range(1, 52)], 'Source data differs from workbook'
    outputs = []
    scenarios = collections.Counter()
    for row in range(2, 52):
        case = f'TC{row - 1:03}'
        assert readable[f'A{row}'] == original[f'A{row}'] == case
        assert readable[f'B{row}'] == original[f'B{row}']
        scenarios[original[f'B{row}']] += 1
        for col in 'CDE':
            assert isinstance(json.loads(original[f'{col}{row}']), dict)
        history = json.loads(original[f'D{row}'])
        for message in history['historical_messages']:
            assert message['text'] in readable[f'D{row}'], case
        if history['current_client_message']:
            assert history['current_client_message']['text'] in readable[f'D{row}'], case
        for col in 'FGH':
            text = readable[f'{col}{row}']
            assert text and text == text.strip()
            assert text == original[f'{col}{row}']
            is_note = text.startswith('【顾问处理建议｜不发送客户】')
            assert is_note == (case == 'TC041')
            outputs.append(text)
    assert len(outputs) == len(set(outputs)) == 150
    assert sorted(scenarios.values()) == [8, 8, 8, 8, 8, 10]
    assert hashlib.sha256(FILE.read_bytes()).hexdigest() == (
        '94126ad7eca1a2d3ce8bddbc02b6292962d2718e62bd361c7fdbbf1800c5ec09')
    print('PASS: 2 sheets; 50 cases; 8 exact headers; 150 distinct outputs.')
    print('PASS: JSON parses; conversation text retained; output columns match.')
    print('147 client-message candidates + 3 no-send notes (TC041).')
    print('PASS: archived SHA-256 matches the delivered final workbook.')


if __name__ == '__main__':
    main()
