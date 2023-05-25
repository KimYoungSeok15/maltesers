<template>
  <div class="backdropcontainer">
    <NavigationBar/>
    <br>
    <div class="container border mycontainer" style="border-radius: 30px; opacity:0.9">
      <br>
      <div class="row">
        <div class="profile_pic_box">
          <img @click="toggleForm()" class="circle custom-cursor" style="width: 300px; height: 300%; object-fit: cover;" src="@/assets/gibone_profile.png" v-if="profile_pic_URL==`http://127.0.0.1:8000null`">
          <img @click="toggleForm()" class="circle custom-cursor" style="width: 300px; height: 300%; object-fit: cover;" :src="profile_pic_URL" v-else>
        </div>
        <br>
        <form id="myForm" style="display: none;" v-if="your_profile_check()">
          <br>
          <input value="파일 선택" style="width:300px" type="file" ref="fileInput"  @change="handleFileChange">
          <button @click="uploadFile">사진 Upload</button>
          <br>
        </form>
        <div>
          <br>
          <br>
          <h2>{{page_user_name}}님의 프로필 페이지</h2>
          <p>가입일 : {{date_joined.slice(0, 10)}} | 가입 시간: {{date_joined.slice(11,19)}}</p>
          <p>경험치 : {{ page_user_point }} exp</p>
          <p>랭크 : {{ rank_check(page_user_point) }}</p>
          <p>다음 랭크까지 남은 경험치 : {{ left_exp }} exp</p>
          <div class="progress-bar">
            <div class="progress row" :style="{ width: (100-left_exp_per*100) + '%' }">
              <span class="col-6 offset-md-4 text-center" style="display: inline-block;">
                {{ 100 - left_exp_per * 100 }}%
              </span>
            </div>
          </div>
        </div>
      </div>
      <br>
      <span>팔로잉: {{how_many_people_page_user_name_follow}}</span> |
      <span>팔로워: {{how_many_people_follow_page_user_name}}</span>
      <br>
      <button v-if="!your_profile_check()" @click="clickFollow" class="btn btn-primary mx-3" :class="follow_status">
        <span>팔로우</span>
      </button>
      <br>
      <br>
      <br>
      <div class="container">
        <div class="row">
          <div class="col-2"></div>
          <p class="px-3 col-2">{{page_user_name}}님의 팔로잉</p>
          <div class="col-2 border content-container" style="height:50px">
            <div class="px-3" v-for="people in how_many_people_page_user_name_follow_list" :key="people.id"><a :href="`http://localhost:8080/profile/${people.following}`">{{people.following}}</a></div>
          </div>
          <p class="col-2">{{page_user_name}}님의 팔로워</p>
          <div class="col-2 border content-container" style="height:50px">
            <div class="px-3" v-for="people in how_many_people_follow_page_user_name_list" :key="people.id"><a :href="`http://localhost:8080/profile/${people.user_name}`">{{people.user_name}}</a></div>
          </div>
        </div>
      </div>  
      <div>
        <br>
        <br>
        <h3>선호 영화 장르</h3>
        <hr>
        <!-- <input  v-if="your_profile_check()" @keypress.enter="addLikeGenre" type="text" placeholder="영화 장르 입력" v-model="like_genre_name"> -->
        <div v-if="your_profile_check()" class="d-flex justify-content-center align-items-center">
          <div class="input-group align-items-center" style="width: 20%;">
          <label class="input-group-text" for="inputGroupSelect01" >장르 선택</label>
            <select class="form-select" id="inputGroupSelect01" v-model="like_genre_name" >
            <!-- <option selected >Choose...</option> -->
            <option value="모험">모험</option>
            <option value="판타지">판타지</option>
            <option value="애니메이션">애니메이션</option>
            <option value="드라마">드라마</option>
            <option value="공포">공포</option>
            <option value="액션">액션</option>
            <option value="코미디">코미디</option>
            <option value="역사">역사</option>
            <option value="서부">서부</option>
            <option value="스릴러">스릴러</option>
            <option value="범죄">범죄</option>
            <option value="다큐멘터리">다큐멘터리</option>
            <option value="SF">SF</option>
            <option value="미스터리">미스터리</option>
            <option value="음악">음악</option>
            <option value="로맨스">로맨스</option>
            <option value="가족">가족</option>
            <option value="전쟁">전쟁</option>
            <option value="TV 영화">TV 영화</option>
            </select>
          </div>
        </div>
        <button  v-if="your_profile_check()" class="btn text-dark btn-outline-dark m-3" @click="addLikeGenre">Add</button>
        <div class="" v-for="genre in like_genre_list" :key="genre.id">
          <span style="font-size: 20px;">{{ genre.genre_name }}</span> <button v-if="your_profile_check()" class="btn text-dark btn-outline-dark p-1" @click="genreDel(genre.id)">Delete</button>
        </div>
      </div>
      <br>
      <div class="container">
        <h3>좋아요한 영화 목록</h3>
        <hr>
        <div class="row">
          <div class="col-3" v-for="movie in like_movie_list" :key=movie.id >
            <router-link :to="`../detail/${movie.movie_id}`"><img class="donggle_poster" :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`"></router-link>
            <br>
            <a :href="`http://localhost:8080/detail/${movie.movie_id}`">{{ movie.movie_name }}</a>
            <br>
            <button  v-if="your_profile_check()" @click="likeMovieDel(movie.id)" class="btn text-dark btn-outline-dark p-1 m-1">Delete</button> 
          </div>
        </div>
      </div>
      <div style="min-height: 30px;"></div>
      <h3>{{page_user_name}}님이 쓴 글</h3>
      <br>
      <div v-if="profile_freeboard_list">
        <div class="" v-for="freeboard_article in profile_freeboard_list" :key="freeboard_article.id">
          <div class="border">
            <a class="underline-on-hover m-0 " @click="GoToFreeDetail(freeboard_article)" >[제목 : {{freeboard_article.title}}] || 작성 시간 : {{freeboard_article.created_at.slice(0, 10)}} {{freeboard_article.created_at.slice(11, 19)}}</a>
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
            is_your_profile: false,
            profile_pic_URL_check: true,

            like_genre_name: '',
            like_genre_list: '',

            like_movie_list: '',

            exp_rank: 'Bronze',
            left_exp_per: 0,
            left_exp: 0,

            progress: 50, // 게이지의 퍼센트 값을 할당

            modalOpen: false, // 모달 상태 저장

            emi_follow: false,

          
        }
    },
    components: {
    NavigationBar,
    },
    computed: {
    progressContainerWidth() {
      return this.progress * 0.4; // 게이지 자체의 가로 크기 계산 (40%)
    },
    },
    methods : {
      openModal() {
      this.modalOpen = true; 
      },
      closeModal() {
        this.modalOpen = false; 
      },
      rank_check(point) {
        if (point < 5000) {
          this.left_exp_per = (5000 - point)/5000
          this.left_exp = 5000 - point
        } else if (point > 5000 && point < 10000) {
          this.exp_rank = 'Silver' 
          this.left_exp_per = (10000 - point)/10000
          this.left_exp = 10000 - point
        } else if (point > 10000 && point < 20000) {
          this.exp_rank = 'Gold'
          this.left_exp = 20000 - point
          this.left_exp_per = (20000 - point)/10000
        } else if (point > 20000 && point < 60000) {
          this.exp_rank = 'Platinum'
          this.left_exp = 60000 - point
          this.left_exp_per = (60000 - point)/40000
        } else if (point > 60000 && point < 100000) {
          this.exp_rank = 'Diamond'
          this.left_exp = 100000 - point
          this.left_exp_per = (100000 - point)/40000
        } else if (point > 100000) {
          this.exp_rank = 'master'
          this.left_exp = 1000000000
          this.left_exp_per = 100
        }
        return this.exp_rank
      },
      toggleForm() {
        const form = document.getElementById("myForm");
        if (form.style.display === "none") {
          form.style.display = "block";
        } else {
          form.style.display = "none";
        }
        
      },
      like_movie_print(user_name) {
        const token = this.$store.state.token
        axios({  
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/Likes/${user_name}/`,
          headers:  {
            Authorization : `Token ${token}`
          },
        })
        .then((res) => {
          console.log(res)
          this.like_movie_list = res.data

        })
        .catch((err) => {
          console.log(err)
          this.like_movie_list = ''
        })
      },
      likeMovieDel(id) {
        const token = this.$store.state.token
        const user_name = this.page_user_name
        axios({  
          method: 'delete',
          url: `http://127.0.0.1:8000/accounts/profile/Likes/del/${id}/`,
          headers:  {
            Authorization : `Token ${token}`
          },
        })
        .then((res) => {
          console.log(res)
          this.like_movie_print(user_name)
        })
      },
      refresh_genre() {
        const user_name = this.page_user_name
        axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/userprofile/user_like_genre/${user_name}/`,
        headers:  {
            Authorization : `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          this.like_genre_list = res.data
        })
        .catch(() => {
          console.log("좋아하는 장르 데이터베이스 빈 값")
          this.like_genre_list = ''
        })
      },
      genreDel(data) {
        const like_genre_id = data
        console.log(typeof like_genre_id)
        axios({
            method: 'delete',
            url: `http://127.0.0.1:8000/accounts/profile/userprofile/user_like_genre_del/${like_genre_id}/`,
            headers:  {
                Authorization : `Token ${this.$store.state.token}`
              }
            })
            .then(() => {
              this.refresh_genre()
            })
      },
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
    // 좋아하는 장르 프로필에 추가
    addLikeGenre() {
      const user_name = this.page_user_name
      const genre_name = this.like_genre_name
      if (genre_name == '') {
        alert("장르를 입력해주세요!")
      } else if ( this.checkGenreNameMatch( this.like_genre_list, genre_name ) ){
        alert("이미 추가한 장르입니다!")
      }
      else {
        axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/profile/userprofile/user_like_genre/${user_name}/`,
        headers:  {
            Authorization : `Token ${this.$store.state.token}`
        },
        data: {
          user_name,
          genre_name
        }
        })
        .then(() => {
          this.like_genre_name=''
          this.refresh_genre()
        })
      }  
    },
    checkGenreNameMatch(like_genre_list, genre_name) {
      for (let i = 0; i < like_genre_list.length; i++) {
        if (like_genre_list[i].genre_name === genre_name) {
          return true;
        }
      }
        return false;
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
    your_profile_check() {
      if (this.$store.state.nowUserName == this.page_user_name) {
        this.is_your_page = true
      }
      return this.is_your_page
    },
    },
  created() {
    // 자유게시판 게시글 작성자 누르면 작성자 이름 받아옴
    const page_user_name_Incoded = document.location.href.split('/')[4]
    this.page_user_name = decodeURIComponent(page_user_name_Incoded)
    const djangoProfile = 'http://127.0.0.1:8000/accounts/profile/userprofile/'
    this.like_movie_print(this.page_user_name)
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/userprofile/user_like_genre/${this.page_user_name}/`,
        headers:  {
            Authorization : `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          console.log(res.data)
          this.like_genre_list = res.data
        })
        .catch((err) => {
          console.log(err)
        })
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
        .catch((err) => {
          console.log(err)
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
        .catch((err)=> {
          console.log(err)
          this.how_many_people_page_user_name_follow = 0
        })
    })
    .catch((err) => {
      console.log(err)
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
            .catch((err) => {
              console.log(err)
            })
    }


  }

</script>

<style scoped>
  .mycontainer {
    min-height: 942.39px;
    background-color: white;
  }

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
  .circle {
    border-radius: 50%;
  }
  .donggle_poster {
    border-radius: 5%;
  }
  .custom-cursor {
  cursor: pointer;
  }
  a {
    text-decoration: none;
    color: black;
  }
  .progress-bar {
  width: 30%;
  height: 20px;
  background-color: #eee;
  margin: 0 auto;
  border-radius: 10px;

}

  .progress {
    height: 100%;
    background-color: skyblue;
  }

  input {
  border-radius: 10px;
  } 
  /* 링크에 마우스가 올라갔을 때 글씨를 볼드체로 변경 */
  a:hover {
    font-weight: bold;
  }
  .backdropcontainer {
  background:url("@/assets/eternal12.jpg");
  opacity: 0.9;
}
</style>
