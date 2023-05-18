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
      axios({  
          method: 'post',
          url: URL,
          data: { title, content },
      })
      .then((response) => {
        console.log('123123')
        console.log(response)
        this.$router.push({name: "community"})
      })
    }
  },
  created() {

  }
}
</script>

<style>

</style>