import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import RandomView from '../views/RandomView.vue'
import weatherRandomView from '../views/weatherRandomView.vue'
import DetailView from '../views/DetailView.vue'
import MainView from '../views/MainView.vue'
import IntroView from '../views/IntroView.vue'
import LoginView from '../views/LoginView.vue'
import SingUpView from '../views/SignUpView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'intro',
    component: IntroView
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
    path: '/community',
    name: 'community',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/CommunityView.vue')
  },
  {
    path: '/weather',
    name: 'weather',
    component: weatherRandomView
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: DetailView
  },
  {
  path: '/login',
  name: 'login',
  component: LoginView
  },
  {
  path: '/signup',
  name: 'signup',
  component: SingUpView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
