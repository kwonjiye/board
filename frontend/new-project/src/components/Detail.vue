<template>
<div>
<div class="content">

		<table class="board_for_read">
			
				<tr>
					<td class="td_title" style="text-align:center; width:20%;">제목</td>
					<td style="padding:10px;">
            <div>{{postlist.title}}</div>

					</td>
				</tr>
				<tr>
					<td class="td_title" style="text-align:center; width:20%;">작성일자</td>
					<td style="padding:10px;">
						<div>{{postlist[0].pub_date}}</div>
					</td>
				</tr>
				<tr>
					<td class="td_title" style="text-align:center;">내용</td>
					<td style="padding:10px;">
            <div>{{postlist[0].text}}</div>
						
					</td>
				</tr>
				
		</table>

			<!-- <div style="text-align:left;">
			
			<form action="{% url 'board:post_like' board.id %}" method="POST">
				{% csrf_token %}
				
				
			</form>



	<div id='result'> {{board.like_count}}</div>
		</div>

		<div style="text-align:left;">
			<a href="{% url 'board:index' %}">> 뒤로가기</a>
		</div>

		<form action="{% url 'board:create_reply' board.id %}" method="post">
		{% csrf_token %}
		<table class="board_for_read">
			
				<tr>
					<td colspan="2" class="td_title" style="text-align:left; padding-left:10px; height:30px;">댓글달기</td>
				</tr>
				<tr>
					<td style="text-align:center;">
						<input type="text" name="comment" id="comment" style="width:100%">
					</td>
					<td><input type="submit" value="save"></td>
				</tr>
			
		</table>
		</form>

		<div class="reply_content">
			{% for rep in board.reply_set.all %}
				<span class="reply">{{ rep.comment }} [{{ rep.rep_date|date:'Y-m-d H:i'}}]</span>
			{% endfor %}
		
 </div>
    </div> -->
 
    
    
    
    <button @click="updateData">수정</button>
    <button @click="deleteData">삭제</button>
    인덱스: {{index}}
    {{contentId}}

		<div style="text-align:left;">
			<router-link to="/">  뒤로가기</router-link>
		</div>

    </div>
  </div>
</template>
<script>
import axios from "axios";
// import data from '@/data'
// import ContentId from '@/router';

export default {

data() {
    return {
    postlist: [],
	name: "Detail",
	// contentId(){
	// 	const index=this.$index.routes.contentId
	// 	return{
	// 		ContentId: ContentId[index]
	// 	}
	// },
		}
	},
  
	created() {
    let url = "http://127.0.0.1:8000/getPost";

    axios({
      method: "GET",
      url: url,
    })
      .then((response) => {
        console.log(this.postlis);
        this.postlist = response.data;
        console.log(response.data);
      })
      .catch((e) => {
        console.log(e);
      });
  }
}
// // data() {
// //     return {
// //    	postlist: [],
// // 	}
// },

//    mounted() {
//     let url = "http://127.0.0.1:8000/";

//     axios({
//       method: "GET",
//       url: url,
//     })
//       .then((response) => {
//         console.log(this.postlis);
//         this.postlist = response.data;
//         console.log(response.data);
//       })
//       .catch((e) => {
//         console.log(e);
//       });
//   }
// };

</script>

<style type="text/css">
        .content {
            max-width:500px;
            margin: auto;
            padding:10px;
            color: black;
            ;
        }

		.reply_content {
            width: 100%;
            font-family: inherit;
            font-size: 100%;
			resize: none;
			border-radius: 0.5em;
			padding-block: 10px;
			border: 0px;
			text-align:right;	
            ;
		}

		.reply_content .reply{
			border-radius: 0.5em;
			display: block;
			margin: 4px;
			padding: 3px 10px;
            background-color: white;
		}

		.board_for_read {
            width:100%;
            font-family: inherit;
            font-size: 100%;
			resize: none;
			border-radius: 0.5em;
			padding-block: 10px;
			border: 0px;
			background-color:#f1f1f1;
		}

		#title {
			height: 32px;
			width: 100%;
			border-radius: 0.5em;
			border: none;
			font-family: inherit;
			font-size: inherit;
			background: none;
            background-color: white;
		}

        textarea {
			width: 100%;
            font-family: inherit;
            font-size: 100%;
			resize: none;
			border-radius: 0.5em;
			padding-block: 10px;
			border: 0px;
            background-color: white;
        }

		.td_title {
            width: 10%;
            font-family: inherit;
            font-size: 100%;
			resize: none;
			border-radius: 0.5em;
			padding-block: 10px;
			border: 0px;
			background-color: #d8d8d8
		}
    </style>