<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container">
        <div class="row">
            <h3 class="">게시글 수정</h3>
            <div>제목</div>
            <input type="text" v-model="updatedTitle" placeholder="제목을 입력해주세요">
            <div>내용</div>
            <input style="height:500px;"  type="text" v-model="updatatedContent" placeholder="내용을 입력해주세요">
            <button @click="updateFreeArticle" class="btn btn-primary col-2 mt-4" value="Add">Add</button>
        </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from "@/components/NavigationBar.vue"
import axios from 'axios'
const UpdateURL = "http://127.0.0.1:8000/api/c1/freeboards/"
const getUsernameURL = "http://127.0.0.1:8000/accounts/user/"
const getWriternameURL = "http://127.0.0.1:8000/api/c1/freeboards/"
export default {
  data(){
    return {
      ArticleId: this.$route.params.id,
      updatedTitle: "",
      updatatedContent: "",
      ArticleWriter: "",
      User: '',
      WriterIsUser: false,    
      token: this.$store.state.token  
    }
  },
  components: {
    NavigationBar
  },
  created(){
        // 현재 로그인된 작성자 가져오기
    axios({ 
      method: 'get',
      url: getUsernameURL,
      headers:  {
      Authorization : `Token ${this.token}`
        },
    })
    .then((response) => {
      this.User = response.data.username
      // 현재 수정하려는 게시물 작성자 가져오기
      axios({ 
        method: 'get',
        url: getWriternameURL + this.ArticleId,
        headers:  {
          Authorization : `Token ${this.token}`
        },
      })
      .then((response) => {
        console.log(response)
        this.ArticleWriter = response.data.user_name       
        if(this.ArticleWriter === this.User){
          this.WriterIsUser = true
        }
      })      
    })
  },
  methods:{
    updateFreeArticle(){  // 게시물 수정 요청
      if (!this.WriterIsUser){
        alert('작성자가 아닙니다!')
        this.router.push({name: "community"})
      }
      else{
      const token = this.token
      const title = this.updatedTitle
      const content = this.updatatedContent
      const user_name = this.User
      axios({  
          method: 'put',
          url: UpdateURL + this.ArticleId + '/',
          data: { title, content, user_name },
          headers: {
          Authorization : `Token ${token}`
          },
      })
      .then((response) => {
        console.log(response)
        this.$router.push({name: "community"})
      })
      }
    }
  }
}
</script>

<style>

</style>