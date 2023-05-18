<template>
  <div>
    <NavigationBar/>    
    <br>
    <h1 class="fw-bold">자유 게시판</h1>
  <router-link to="/createfreearticle" class="btn btn-primary my-5"> 게시글 작성 </router-link>    
    <div class="container">
      <div class="row">
        <div class="col-1"></div>
        <div class="col-10">
           <p class="m-0" v-for="article in articleAll" :key="article.id" style="border: solid 1px;">
            <span @click="GoToFreeDetail(article.id)" class="col-5 mx-5">제목: {{ article.title }}</span> <br>
            <span class="col-5 mx-5">article.id: {{ article.id }}</span> <br>
            <span class="col-5 mx-5">생성시간 : {{ article.created_at }}</span>
        </p>
        </div>
       
      </div>
    </div>
    

    <br><br><br><br><br><br><br><br><br><br>
    <!-- <CommunityListForm/>
    <CommunityListItem/> -->
  </div>
</template>

<script>
// import CommunityListForm from '@/components/CommunityListForm.vue'
// import CommunityListItem from '@/components/CommunityListItem.vue'
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'

export default {
  name: 'CommunityView',
  components: {
    // CommunityListForm, 
    // CommunityListItem,
    NavigationBar,
  },
  data() {
    return {
			articleAll: ''
		}
	},
  // 전체 게시글을 Django DB에서 받아와서 Store에 저장
  created() {
    const djangoCommunity = 'http://127.0.0.1:8000/api/c1/freeboards/'
    axios({
        methods: 'get',
        url: djangoCommunity,
    })
    .then((response) => {
      this.articleAll = response.data
      console.log(this.articleAll)
    })
  },
  methods: {
    GoToFreeDetail(data){
      this.$router.push({name:'communityfreedetail', params: {id: data}})
      // this.$router.go()
    }
  }
}
</script>

<style>

</style>