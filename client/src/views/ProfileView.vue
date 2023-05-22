<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container border">
      <br>
      <div class="row">
        <form>
          <input type="file" ref="fileInput"  @change="handleFileChange">
          <button @click="uploadFile">Upload</button>
        </form>
        <div class="profile_pic_box">
          <img style="width: 100px; height: 200%; object-fit: cover;" :src="profile_pic_URL" alt="">
        </div>
        <br>
        <h1>{{page_user_name}}님의 프로필 페이지</h1>
        <p>가입일 : {{date_joined.slice(0, 10)}} | 가입 시간: {{date_joined.slice(11,19)}}</p>
        <p>포인트 : {{ page_user_point }}</p>
        <div class=""></div>
      </div>
      <button @click="clickFollow" class="btn btn-primary mx-3" :class="follow_status">팔로우</button>
      <span>{{page_user_name}}님이 팔로우하고 있는 사람: {{how_many_people_page_user_name_follow}}</span> |
      <span>{{page_user_name}}님을 팔로잉하는 사람: {{how_many_people_follow_page_user_name}}</span>
      <br>
      <br>
      <br>
      <!-- <div class="container">
        <div class="row">
          <p class="col-3">{{page_user_name}}님이 팔로우하고 있는 사람 목록</p>
          <div class="content-container col-3" v-for="people in how_many_people_follow_page_user_name_list" :key="people.id">
            <p>{{people.user_name}}</p>
          </div>
          <p class="col-3">{{page_user_name}}님을 팔로우하고 있는 사람 목록
          <div class="content-container col-3" v-for="people in how_many_people_page_user_name_follow_list" :key="people.id">
            <p>{{people.following}}</p>
          </div>
        </div>
      </div>   -->
      <br>
      <h3>{{page_user_name}}님이 쓴 글</h3>
      <div v-if="profile_freeboard_list">
        <div class="" v-for="freeboard_article in profile_freeboard_list" :key="freeboard_article.id">
          <div class="border">
            <p class="underline-on-hover m-0" @click="GoToFreeDetail(freeboard_article)" >[제목 : {{freeboard_article.title}}] || 작성 시간 : {{freeboard_article.created_at.slice(0, 10)}} {{freeboard_article.created_at.slice(11, 19)}}</p>
          </div>
        </div>
      </div>
      <div v-else>
        <p>{{page_user_name}}님이 작성한 글이 없습니다. </p>
      </div>
    </div>
    <div>
      
    </div>
    

  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'

export default {
    name: 'ProfileView',
    data() {
        return {
            page_user_name : '',
            date_joined: '',
            page_user_point: 0,
            current_page : document.location.href,
            profile_freeboard_list : '',
            how_many_people_follow_page_user_name : 0, // 현재 페이지 사람울 팔로우한 사람 수
            how_many_people_follow_page_user_name_list : [' '],
            how_many_people_page_user_name_follow : 0, // 현재 페이지 사람이 팔로우한 사람 수
            how_many_people_page_user_name_follow_list : [' '],
            follow_status : '111111',
            selectedFile: null,
            profile_pic_URL: '',
          
        }
    },
    components: {
    NavigationBar,
    },
    
    methods : {
      handleFileChange(event) {
      this.selectedFile = event.target.files[0];
      },
      uploadFile(event){
          event.preventDefault()
          console.log(this.selectedFile)
          if (this.selectedFile) {
          const formData = new FormData();
          formData.append('file', this.selectedFile);
          try {
            const {data} = axios.put(`http://127.0.0.1:8000/accounts/profile/userprofile/put/${this.page_user_name}/`, formData, {
              headers: {
                Authorization : `Token ${this.$store.state.token}`
              }
            });
            console.log(data)
            axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/profile/userprofile/${this.page_user_name}/`,
            headers:  {
                Authorization : `Token ${this.$store.state.token}`
              }
            })
            .then(() => {
              this.$router.go();
              
            })
            
          } catch(err) {
            console.log(err)
          }
      }
    },
      clickFollow() {
        const user_name = this.$store.state.nowUserName
        const following = this.page_user_name
        axios({
          method: 'post',
          url: "http://127.0.0.1:8000/accounts/profile/followings/",
          headers:  {
              Authorization : `Token ${this.$store.state.token}`
          },
          data: {
            user_name,
            following
          }
        })
      .then(() => {
        alert("팔로우 완료")
        // 현재 페이지 사용자 팔로우 한 사람 수 갱신
       
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/followings/count/${this.page_user_name}/`,
          headers:  {
              Authorization : `Token ${this.$store.state.token}`
          },
        })
        .then((response) => {
          console.log(response)
          this.how_many_people_follow_page_user_name = response.data[0].following_count
        })
      })
      .catch((error) => {
        if (error.response.status === 400 && error.response.data.error === '자기 자신을 팔로우할 수 없습니다.') {
      // 자기 자신을 팔로우하려고 한 경우
          alert('자기 자신을 팔로우할 수 없습니다.');
        } else {
          alert('이미 팔로우한 사용자입니다.')
        }
      })
      },
      GoToFreeDetail(data){
        this.$router.push({name:'ReviewDetail', params: {id: data.id}})
        
        // this.$router.go()
      },
    },
  created() {
    // 자유게시판 게시글 작성자 누르면 작성자 이름 받아옴
    const page_user_name_Incoded = document.location.href.split('/')[4]
    this.page_user_name = decodeURIComponent(page_user_name_Incoded)
    const djangoProfile = 'http://127.0.0.1:8000/accounts/profile/userprofile/'

    axios({
        methods: 'get',
        url: djangoProfile+`${this.page_user_name}`,
        headers:  {
            Authorization : `Token ${this.$store.state.token}`
        },
    })
    .then((response) => {
        this.date_joined = response.data.date_joined
        this.page_user_point = response.data.point
        axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/c1/profile/freeboards/'+`${this.page_user_name}/`,
        headers:  {
            Authorization : `Token ${this.$store.state.token}`
        }
        })
        .then((response) => {
          console.log(response)
          this.profile_freeboard_list = response.data
        })
        .catch(() => {
          this.profile_freeboard_list = ''
        })
        // 처음 프로필 페이지 불러올 때 현재 페이지 사용자 팔로우 한 사람 수 갱신
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/followings/count/${encodeURIComponent(this.page_user_name)}/`,
          headers:  {
              Authorization : `Token ${this.$store.state.token}`
          },
        })
        .then((response) => {
          console.log(response)
          this.how_many_people_follow_page_user_name = response.data[0].following_count
          this.how_many_people_follow_page_user_name_list = response.data[0].following_list
        })
        .catch(() => {
          this.how_many_people_follow_page_user_name = 0
        })
        // 처음 프로필 페이지 불러올 때 현재 페이지 사용자가 팔로우한 사람 수 갱신
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/followers/count/${encodeURIComponent(this.page_user_name)}/`,
          headers:  {
              Authorization : `Token ${this.$store.state.token}`
          },
        })
        .then((response) => {
          console.log(response)
          this.how_many_people_page_user_name_follow = response.data[0].following_count
          this.how_many_people_page_user_name_follow_list = response.data[0].following_list
        })
        .catch(()=> {
          this.how_many_people_page_user_name_follow = 0
        })
    })
    axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/profile/userprofile/${this.page_user_name}/`,
            headers:  {
                Authorization : `Token ${this.$store.state.token}`
              }
            })
            .then((res) => {
              console.log(res.data.profile_pic)
              this.profile_pic_URL = `http://127.0.0.1:8000${res.data.profile_pic}`
              console.log(this.profile_pic_URL)
              
            })
    }


  }

</script>

<style>
  .content-container {
    height: 50px; /* 원하는 높이 설정 */
    overflow: auto; /* 스크롤바를 추가하기 위해 overflow 속성 사용 */
  }
  .profile_pic_box {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
  }
</style>