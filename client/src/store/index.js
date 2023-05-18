import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    allMovies: {},
    topRatedMovies: {},
    randomPickData: null,
    wannaWatch: [],
  },
  getters: {
  },
  mutations: {
    GET_ALL_MOVIES(state, allMovies) {
      state.allMovies = allMovies
    },
    TOPRATED_MOVIES(state, ml) {
      state.topRatedMovies = ml
    },
    WANNA_MOVIES(state, mN) {
      state.wannaWatch.push({mN, is_completed: false})
    },
  },
  actions: {
    getAllMovies(context, AllMovies) {
      context.commit('GET_ALL_MOVIES', AllMovies)
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
