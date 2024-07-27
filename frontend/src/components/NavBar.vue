<template>
  <nav class="bg-blue-500 p-4">
    <ul class="flex space-x-4">
      <li><router-link to="/" class="text-white">Inicio</router-link></li>
      <li><router-link to="/reservas" class="text-white">Reservas</router-link></li>
      <li><router-link to="/administradores" class="text-white">Administradores</router-link></li>
      <li><router-link to="/socios" class="text-white">Socios</router-link></li>
      <li><router-link to="/pistas" class="text-white">Pistas</router-link></li>
      <li><router-link to="/mis-reservas" class="text-white">Mis Reservas</router-link></li>
      <li><router-link to="/login" class="text-white">Login</router-link></li>
      <li><router-link to="/register" class="text-white">Register</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style scoped>
/* Estilos adicionales si es necesario */
</style>