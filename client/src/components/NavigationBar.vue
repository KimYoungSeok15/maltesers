<template>
	<nav class="d-flex justify-content-around m-310" style="position:sticky;top:0;height:auto;min-height:90px;max-height:20px;z-index:1;background:rgb(130,130,130); opacity: 0.9;">
		<div class="">
			<img src="@/assets/hooni2.png" @click="GoMain" style="height: 40px; width: 100px;" class="" alt="">		
		</div>
		<span class="mt-2">
			<router-link style="text-decoration: none;" to="/main">Main</router-link> |
			<router-link style="text-decoration: none;" to="/movies">Movie</router-link> |
			<router-link style="text-decoration: none;" to="/random">Random</router-link> |
			<router-link style="text-decoration: none;" to="/review">Reviews</router-link> |
			<router-link style="text-decoration: none;" to="/weather">Today's Recommended Movie</router-link>
		</span>
    <span class="">
		<a class="btn mx-3 btn-outline-light" @click="GoProfile">{{user}}</a>
		<a href="/" @click="logout" class="btn mx-3 btn-outline-light">logout</a>
		<router-link class="btn mx-3 btn-outline-light" to="/signup">SignUp</router-link>
    </span>
	</nav>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			user : this.$store.state.nowUserName,
	
			
		}
	},
	methods:{
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
			this.$router.push({name:'profile', params: {username: this.user}})
			this.$router.go()
		},
		GoMain() {

			this.$router.push({ name : 'main'})
			this.$router.go()
		}
	},
	created() {
		console.log(this.current_page)
	}
}
</script>
<style>
</style>