import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'

Vue.use(Vuex)
import createPersistedState from 'vuex-persistedstate'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    allMovies: {},
    topRatedMovies: {},
    randomPickData: null,
    wannaWatch: [],
    token: null,
    nowUserName: '',
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false 
      // 토큰이 있으면 true 없으면 false
    }
  },
  mutations: {
    GET_FREEARTICLES(state, articles) {
      state.articles = articles
    },
    SIGN_UP(state, token) {
      state.token = token
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'main'})
    },
    GET_ALL_MOVIES(state, allMovies) {
      state.allMovies = allMovies
    },
    TOPRATED_MOVIES(state, ml) {
      state.topRatedMovies = ml
    },
    WANNA_MOVIES(state, mN) {
      state.wannaWatch.push({mN, is_completed: false})
    },
    LOGOUT(state){
      state.token = null
    },
    SAVE_USERID(state, username){
      state.nowUserName = username
    }
  },
  actions: {
    getfreeArticles(context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/c1/freeboards`,
        headers:  {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_FREEARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    getAllMovies(context, AllMovies) {
      context.commit('GET_ALL_MOVIES', AllMovies)
    },
    topRatedMovies(context, topRatedMoviesList) {
      context.commit('TOPRATED_MOVIES', topRatedMoviesList)
    },
    createWannaWatchMovie(context, movieName) {
      context.commit('WANNA_MOVIES', movieName)
    },
    signUp(context, payload) {
      const username = payload.username
      const user_name = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: {
          username,  password1,  password2
        }
      })
      .then(res => {
        console.log(res)
        // context.commit('SIGN_UP', res.data.key)
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERID', username)
        var current_datetime = new Date();
        var formatted_datetime = current_datetime.toISOString().slice(0, -1);
        
        // 한국 표준시간대(KST)와의 차이를 계산합니다. (분 단위)
        var kstOffset = 18 * 60; // 한국은 UTC+9
        
        // 현재 시간에 한국 표준시간대(KST)와의 차이를 적용합니다.
        var date_joined = new Date(formatted_datetime);
        date_joined.setMinutes(date_joined.getMinutes() + kstOffset);
        const point = 0
        
        
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/accounts/profile/userprofile/${user_name}/`,
          data: {
            user_name, date_joined, point
          }
        })
      })
      .catch(err => console.log(err))
    },

    LogIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: "http://127.0.0.1:8000/accounts/login/",
        data: {
          username,  password
        }
      })
      .then(res => {
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERID', username)
      })
      .catch(err => console.log(err))   
    },

    logout(context){
      context.commit('LOGOUT')
    }
  },
  modules: {
  }
})
