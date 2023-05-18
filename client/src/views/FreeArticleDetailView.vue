<template>
  <div>
    <NavigationBar/>
    <p>제목 : {{ArticleTitle}}</p>
    <p>내용 : {{ArticleContent}}</p>
    <p v-if="ArticleUpdatedAt"> 작성일자 : {{ArticleUpdatedAt}}</p>
    <p v-if="ArticleCreatedAt"> 수정일자 : {{ArticleCreatedAt}}</p>
    <router-link to="/community">뒤로가기</router-link>
  </div>
</template>
      

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'
const URL = `http://127.0.0.1:8000/api/c1/freeboards/`
export default {
  components: {
    NavigationBar,
  },
  data(){
    return{
      ArticleId: this.$route.params.id,
      ArticleTitle: '',
      ArticleContent: '', 
      ArticleCreatedAt: '', 
      ArticleUpdatedAt: '' 
    }
  },
  created() {
    axios({  
				methods: 'get',
				url: URL + this.ArticleId
		})
		.then((response) => {
      this.ArticleTitle = response.data.title
      this.ArticleContent = response.data.content
      this.ArticleCreatedAt = response.data.created_at
      this.ArticleUpdatedAt = response.data.updated_at
		})
  }
}
</script>

<style>

</style>
