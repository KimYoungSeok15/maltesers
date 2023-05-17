import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    mainTopMovies: {},
    playingMovies: {},
    upComingMovies: {},
    topRatedMovies: {},
    randomPickData: null,
    wannaWatch: [],
  },
  getters: {
  },
  mutations: {
    MAIN_TOP_MOVIES(state, toplist) {
      state.mainTopMovies = toplist
    },
    PLAYING(state, playinglist) {
      state.playingMovies = playinglist
    },
    UPCOMING(state, upcoming) {
      state.upComingMovies = upcoming
    },
    TOPRATED_MOVIES(state, ml) {
      state.topRatedMovies = ml
    },
    WANNA_MOVIES(state, mN) {
      state.wannaWatch.push({mN, is_completed: false})
    },
  },
  actions: {
    mainTopMovies(context, mainTopMovies) {
      context.commit('MAIN_TOP_MOVIES', mainTopMovies)
    },
    mainPlaying(context, playing) {
      context.commit('PLAYING', playing)
    },
    upComing(context, upComing) {
      context.commit('UPCOMING', upComing)
    },
    topRatedMovies(context, topRatedMoviesList) {
      context.commit('TOPRATED_MOVIES', topRatedMoviesList)
    },
    createWannaWatchMovie(context, movieName) {
      context.commit('WANNA_MOVIES', movieName)
    },
  },
  modules: {
  }
})
