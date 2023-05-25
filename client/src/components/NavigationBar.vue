<template>
	<nav class="d-flex justify-content-around m-310 pt-4" :style="{ opacity : navOpacity,  transition: 'opacity 1.5s'}">
			<img src="@/assets/hooni3.png" @click="GoMain" style="height: 47px; width: 100px; cursor: pointer;" class="" alt="">		
		<span class="mt-2" id="links">
			<router-link style="text-decoration: none;" to="/main">Main</router-link> |
			<router-link style="text-decoration: none;" to="/movies">Movie</router-link> |
			<router-link style="text-decoration: none;" to="/random">Random</router-link> |
			<router-link style="text-decoration: none;" to="/review">Reviews</router-link> |
			<!-- <router-link style="text-decoration: none;" to="/weather">날씨 랜덤 무비</router-link> | -->
			<router-link style="text-decoration: none;" to="/recommend">Recommended Movie</router-link>
		</span>
    <span class="">
		<a :href="`http://localhost:8080/profile/${user}`" class="mx-3">
			<img class="circle" style="width: 40px; height: 40px; object-fit: cover;" src="@/assets/gibone_profile.png" v-if="profile_pic_URL==`http://127.0.0.1:8000null`">
			<img class="circle" style="width: 40px; height: 40px; object-fit: cover;" :src="profile_pic_URL" v-else >
		</a>
		<!-- <a class="btn mx-3 btn-outline-light" @click="GoProfile">{{user}}</a> -->
		<a href="/" @click="logout" class="btn mx-3 btn-outline-light">logout</a>
    </span>
	</nav>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			user : this.$store.state.nowUserName,
			navOpacity: 1.0,
			timer: null,
			profile_pic_URL: '',
		}
	},
	mounted() {
			window.addEventListener('wheel', this.handleMouseWheel);
		},
  beforeUnmount() {
    window.removeEventListener('wheel', this.handleMouseWheel);
  },	
	methods:{
		getProfilePic() {
			console.log(this.$store.state.nowUserName)
			axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/profile/userprofile/${this.$store.state.nowUserName}/`,
            headers:  {
                Authorization : `Token ${this.$store.state.token}`
              }
            })
            .then((res) => {
              console.log(res.data.profile_pic, 'adsasdasdasd')
              this.profile_pic_URL = `http://127.0.0.1:8000${res.data.profile_pic}`
              console.log(this.profile_pic_URL)
              
            })
            .catch((err) => {
              console.log(err)
            })
		},
		logout() {		
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/accounts/logout/',
				headers:  {
					Authorization: `Token ${this.$store.state.token}`
				}
			})
			this.$store.dispatch('logout')
			},
		GoProfile() {
			// 여기에서 인코딩된 입력값을 전송하거나 처리할 수 있습니다.
			this.$router.push({name:'profile', params: {username: this.user}})
			this.$router.go()
		},
		GoMain() {
			if (this.$route.path != '/main'){
			this.$router.push({ path : '/main'})				
			this.$router.go()
			}
		},
		handleMouseWheel() {
      // 마우스 이동 이벤트 처리
			this.navOpacity = 0.0
      clearTimeout(this.timer); // 이전 타이머 제거
      this.timer = setTimeout(() => {
        this.navOpacity = 1.0; // 초기값으로 되돌림
      }, 250); // 원하는 시간으로 설정 (여기서는 2초로 설정)
    },		
	},
	created() {
		console.log(this.current_page)
		this.getProfilePic()
	}
}
</script>
<style>
nav {
	position:sticky;
	z-index:1;
	top:0;
	height:auto;
	min-height:90px;
	max-height:20px;
	background:rgb(0, 0, 0);
	transition: transform 0.3s ease;
	font-size: 20px;
}
nav:hover {
  opacity: 0.9;
	z-index: 2;	
	/* background:rgb(143, 143, 143);	 */
}
.circle {
    border-radius: 50%;
  }
</style>