import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Reservas from '../views/Reservas.vue'
import Administradores from '../views/Administradores.vue'
import Socios from '../views/Socios.vue'
import Pistas from '../views/Pistas.vue'
import MisReservas from '../views/MisReservas.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/reservas', component: Reservas },
  { path: '/administradores', component: Administradores },
  { path: '/socios', component: Socios },
  { path: '/pistas', component: Pistas },
  { path: '/mis-reservas', component: MisReservas },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router