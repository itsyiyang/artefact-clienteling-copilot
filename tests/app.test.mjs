import {test} from 'node:test';import assert from 'node:assert/strict';import {validateGeneration,validateJudge} from '../server.mjs';
import {checkQuotes} from '../server.mjs';
test('Judge cannot pass with invented evidence',()=>{const j=checkQuotes({verdict:'通过当前检查',issues:[{candidate:1,quote:'不存在',rule:'R01',severity:'verify'}]},{candidates:[{text:'您好'}]});assert.equal(j.verdict,'需核实');assert.equal(j.invalidIssues.length,1);});
test('three candidates required unless explicitly blocked',()=>{assert.throws(()=>validateGeneration({eligibility:'appropriate',reason:'',candidates:[]}));assert.doesNotThrow(()=>validateGeneration({eligibility:'blocked',reason:'拒绝营销',candidates:[]}));});
test('hard failure cannot be masked by high scores',()=>{const j=validateJudge({verdict:'通过当前检查',scores:{grounding:5,relationship:5,personalization:5,diversity:5},issues:[{severity:'must_fix'}]});assert.equal(j.verdict,'需修改');assert.throws(()=>validateJudge({scores:{}}));});
