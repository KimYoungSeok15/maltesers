<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container">
        <div class="row">
            <h3 class="">게시글 등록</h3>
            <div>제목</div>
            <input type="text" v-model="freeTitle" placeholder="제목을 입력해주세요">
            <div>내용</div>
            <input style="height:500px;"  type="text" v-model="freeContent" placeholder="내용을 입력해주세요">
            <button @click="postFreeArticle" class="btn btn-primary col-2 mt-4" value="Add">Add</button>
        </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from "@/components/NavigationBar.vue"
import axios from 'axios'
const getUsernameURL = "http://127.0.0.1:8000/accounts/user/"
const URL = "http://127.0.0.1:8000/api/c1/freeboards/"
export default {
  data(){
    return {
      freeTitle:"",
      freeContent:""
    }
  },
  components: {
    NavigationBar
  },
  methods:{
    postFreeArticle(){
      const title = this.freeTitle
      const content = this.freeContent     
      const token = this.$store.state.token
      let user_name = ''
      axios({  
          method: 'get',
          url: getUsernameURL,
          headers:  {
          Authorization : `Token ${token}`
          },
      })
      .then((response) => {
        user_name = response.data.username
        console.log(user_name)
        axios({  
            method: 'post',
            url: URL,
            data: { title, content, user_name },
            headers:  {
            Authorization : `Token ${token}`
            },
        })
        .then((response) => {
          console.log(response)
          this.$router.push({name: "community"})
        })        
      })


    }
  },
  created() {

  }
}
</script>

<style>

</style>