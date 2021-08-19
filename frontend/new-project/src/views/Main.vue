<template>
 <div>
    <div style="text-align: center">
      <div id="app">
        <Header />

        <h1>게시판 만들기</h1>
        <div class="content">
          <div style="text-align: right">
              <div action=""> 
                <inputField :name="name" @update-name="updateName" />
                <!-- <inputField /> -->
                <br><button>submit</button>
              </div>
              {{ name }}
                <router-link to='board2'><button>글쓰기</button></router-link>
             
          </div>
        </div>

        <div id="tableBoard" style="text-align: center; margin: 5px">
          <table class="board">
            <thead>
              <tr class="header">
                <th>순번</th>
                <th>작성자</th>
                <th style="width: 15%">제목</th>
                <th>내용</th>
                <th>좋아요</th>
                <th>작성일자</th>
                <th>조회수</th>
                <th>내용보기</th>
              </tr>
            </thead>
            <tr :key="index" v-for="(value, index) in postlist" >
              <td>{{value.id}}</td>
               <td>{{ value.author }}</td>
               <td>{{ value.title }}</td>
               <td>{{ value.text }}</td>
              <td style=" width: 100px">{{ value.like_count }}<button @click="value.like_count+=1">좋아요</button></td>
              <td> {{ value.pub_date }}</td>
              <td> {{ value.update_counter }} </td>
              <td style="width: 100px"> <button @click="detail(index)">내용보기</button></td>
            </tr>
          </table>
        </div>
        <paginated-list :list-array="postlist"/>
        
  <!-- <div class="overflow-auto">
    <b-table striped hover: url="url" :fields="fields" @row-clicked="rowClick"><b-table>
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
    ></b-pagination> -->
<!-- 
  </div> -->

        
      </div>
    </div>
  </div>

</template>
<script>
import inputField from '@/views/inputField'
//import BoardForm from './componenets/BoardForm';
import Header from '@/views/Header'
import axios from "axios";
import paginatedList from '@/views/PaginatedList';
// import detail from '@/components/Detail'


export default{

  components:{
    inputField,
    Header,
    paginatedList
   
    //BoardForm,
  },

  
  data() {
    return {
      postlist: [],
      pageNum: 0,
      name:" ",
      step:1,
      // currentPage: 1,
      // perpage:10
    };
  },
  
  methods : {  
    detail(index){
    this.$router.push({
      name:'Detail',
      params: {
        contentId: index
           }
        })
       }
    },
  // computed :{

  //   rows(){
  //     return this.items.length
  //   }
  // },

//  props: {
//     listArray: {
//       type: Array,
//       required: true,
//     },
//     pageSize: {
//       type: Number,
//       required: false,
//       default: 10,
//     },
//   },
//   methods: {
//     nextPage() {
//       this.pageNum += 1;
//     },
//     prevPage() {
//       this.pageNum -= 1;
//     },

//     updateName(name){
//       this.name = name;
//     }
//   },
  mounted() {
    let url = "http://127.0.0.1:8000";

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
</script>




<style type="text/css">
.header {
  top: 0;
  height: 60px;
  width: 100%;
  /* position: fixed; */
  /* z-index:1; */
  background-color: #2b7b8d;
  /* overflow: hidden; */
  /* display: flex; */
  justify-content: left;

  border-radius: 10px;
  margin: 50px;
}
.header a {
  padding: 100px;
  width: 100%;
}

.multiline-ellipsis {
  height: 60px;
  width: 100%;
  padding: 10px;
  margin: 50px;
  overflow: hidden;
  width: 10%;
}

.multiline-ellipsis a {
  padding: 10px;
}

.content.center {
  display: flex;
  align-items: center;
}

.content a {
  text-align: center;
  margin: 0px 5px 0px 5px;
}

a {
  color: black;
  text-decoration: none;
  font-size: 18px;
}

a:hover {
  color: black;
}

.sidemenu {
  height: 100%;
  width: 200px;
  position: fixed;
  z-index: 1;
  top: 60px;
  left: 0;
  background-color: #02343f;
  overflow-x: hidden;
  padding-top: 20px;
}

.sidemenu li {
  margin: 10px;
}

.wrap_content {
  margin-top: 70px;
  margin-left: 210px;
  margin-right: 10px;
}

ul {
  list-style: none;
  list-style-position: outside;
}

body {
  margin: 0px;
  background-color: #f0edcc;
}

.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
</style>
