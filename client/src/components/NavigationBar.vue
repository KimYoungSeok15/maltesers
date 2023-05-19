<template>
	<nav class="d-flex justify-content-around" style="position:sticky;top:0;height:auto;min-height:70px;max-height:20px;z-index:1;background:rgb(150,150,150);">
		<div>
			<img src="@/assets/hooni2.png" style="height: 40px;" class="" alt="">		
		</div>
		<span>
			<router-link to="/main">Main</router-link> |
			<router-link to="/movies">Movie</router-link> |
			<router-link to="/random">Random</router-link> |
			<router-link to="/community">Community</router-link> |
			<router-link to="/weather">Today's Recommended Movie</router-link>
		</span>
    <span>
      <a href="/" @click="logout" class="mx-3">logout</a>
      <router-link class="mx-3" to="/signup">SignUp</router-link>
    </span>
	</nav>
</template>

<script>
import axios from 'axios'
export default {
	methods:{
		logout() {		
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/api/m1/movies/',
				headers:  {
					Authorization: `Token ${this.$store.state.token}`
				}
		})
		this.$store.dispatch('logout')
		}
	}
}
</script>
<style>
</style>