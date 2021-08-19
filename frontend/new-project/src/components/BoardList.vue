<template>
	<div>
		<h1>게시판 등록</h1>

		<div class="AddWrap">
			<form>
				<table class="tbAdd">
					<colgroup>
						<col width="15%" />
						<col width="*" />
					</colgroup>
					<tr>
						<th>제목</th>
						<td><input type="text" v-model="subject" ref="subject" /></td>
					</tr>
					<tr>
						<th>내용</th>
						<td><textarea v-model="cont" ref="cont"></textarea></td>
					</tr>
				</table>
			</form>
		</div>

		<div class="btnWrap">
			<a href="javascript:;" @click="fnList" class="btn">목록</a>
			<a href="javascript:;" @click="fnAddProc" class="btnAdd btn">등록</a>
		</div>	
	</div>
</template>

<script>
import axios from "axios";
export default {

	
	data() { //변수 생성
		return{
			board_code:'news'
			,subject:''
			,cont:''
			,id:'admin'
			,form:'' //form 전송 데이터
		}
	}
	,methods:{

		
		fnList(){ //리스트 화면으로 이동 함수
			this.$router.push({path:'./',query:this.body});
			
		}

		
		,fnAddProc: function() { //등록 프로세스
			if(!this.subject) { //제목이 없다면 값을 입력하라고 알려준다.
				alert("제목을 입력해 주세요");
				this.$refs.subject.focus(); //방식으로 선택자를 찾는다.
				return;
			}

			let url = "http://127.0.0.1:8000/Post";

			axios({
				method: 'POST',
				url:url,
				data: this.data
			})
			.then((response)=>{
				this.postlist=response.data;
				this.$emit('saved')
			})
			.catch((err)=>{
				console.log(err);
			})
			
		}
	}	
}
</script>

<style scoped>
	.tbAdd{border-top:1px solid #888;}
	.tbAdd th, .tbAdd td{border-bottom:1px solid #eee; padding:5px 0;}
	.tbAdd td{padding:10px 10px; box-sizing:border-box;}
	.tbAdd td input{width:100%; min-height:30px; box-sizing:border-box; padding:0 10px;}
	.tbAdd td textarea{width:100%; min-height:300px; padding:10px; box-sizing:border-box;}
	.btnWrap{text-align:center; margin:20px 0 0 0;}
	.btnWrap a{margin:0 10px;}
	.btnAdd {background:#43b984}
	.btnDelete{background:#f00;}
</style>