import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import RandomView from '../views/RandomView.vue'
import weatherRandomView from '../views/weatherRandomView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import MainView from '../views/MainView.vue'
import IntroView from '../views/IntroView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import JsonTestView from '../views/JsonTestView.vue'
import ReviewCreateView from '../views/ReviewCreateView.vue'
import ReviewUpdateView from '../views/ReviewUpdateView.vue'
import ReviewDetailView from '../views/ReviewDetailView.vue'
import ReviewView from '../views/ReviewView.vue'
import Profile from '../views/ProfileView.vue'
import recommend from '../views/RecommendView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/recommend',
    name: 'recommend',
    component: recommend
  }, 
  {
    path: '/profile/:username',
    name: 'profile',
    component: Profile
  }, 
  {
    path: '/',
    name: 'intro',
    component: IntroView
  }, 
  {
    path: '/jsontest',
    name: 'jsontest',
    component: JsonTestView
  }, 
  {
    path: '/main',
    name: 'main',
    component: MainView
  },
  {
    path: '/movies',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/random',
    name: 'random',
    component: RandomView
  },
  {
    path: '/review',
    name: 'review',
    component: ReviewView
  },
  {
    path: '/review/:id',
    name: 'ReviewDetail',
    component: ReviewDetailView
  },
  {
    path: '/weather',
    name: 'weather',
    component: weatherRandomView
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: MovieDetailView
  },
  {
    path: '/reviewcreate/:movie_title',
    name: 'reviewcreate',
    component: ReviewCreateView
  },  
  {
    path: '/review/:id/update',
    name: 'reviewupdate',
    component: ReviewUpdateView
  },  
  {
  path: '/login',
  name: 'login',
  component: LoginView
  },
  {
  path: '/signup',
  name: 'signup',
  component: SignUpView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
