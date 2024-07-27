<template>
  <div>
    <h1 class="text-3xl mb-4">Administradores</h1>
    <div class="card mb-4">
      <h2 class="text-2xl mb-2">Crear Nuevo Administrador</h2>
      <label for="admin-nombre" class="block">Nombre</label>
      <input id="admin-nombre" name="admin-nombre" v-model="nuevoAdmin.nombre" placeholder="Nombre" class="input mb-2"/>
      <label for="admin-password" class="block">Contraseña</label>
      <input id="admin-password" name="admin-password" v-model="nuevoAdmin.password" type="password" placeholder="Contraseña" class="input mb-2"/>
      <button @click="crearAdministrador" class="btn btn-blue">Crear</button>
    </div>
    <div v-for="admin in administradores" :key="admin.id" class="card mb-4">
      <h2 class="text-2xl mb-2">{{ admin.nombre }}</h2>
      <button @click="editarAdministrador(admin)" class="btn btn-blue">Modificar</button>
      <button @click="eliminarAdministrador(admin.id)" class="btn btn-red">Eliminar</button>
      <button @click="cancelarEdicion" class="btn btn-gray">Cancelar</button>
    </div>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'Administradores',
  data() {
    return {
      administradores: [],
      nuevoAdmin: {
        nombre: '',
        password: ''
      }
    }
  },
  mounted() {
    this.fetchAdministradores();
  },
  methods: {
    async fetchAdministradores() {
      try {
        const response = await api.getAdministradores();
        this.administradores = response.data;
      } catch (error) {
        console.error("Error fetching administradores:", error);
      }
    },
    async crearAdministrador() {
      try {
        await api.createAdministrador(this.nuevoAdmin);
        this.fetchAdministradores();
        this.nuevoAdmin = {
          nombre: '',
          password: ''
        };
      } catch (error) {
        console.error("Error creating administrador:", error);
      }
    },
    editarAdministrador(admin) {
      // Implementa la lógica para editar administrador
    },
    async eliminarAdministrador(id) {
      try {
        await api.deleteAdministrador(id);
        this.fetchAdministradores();
      } catch (error) {
        console.error("Error deleting administrador:", error);
      }
    },
    cancelarEdicion() {
      // Implementa la lógica para cancelar la edición y volver a la vista principal
    }
  }
}
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  padding: 16px;
  border-radius: 8px;
  background-color: #f9f9f9;
}
.input {
  width: 100%;
  padding: 8px;
  margin-bottom: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.btn {
  padding: 8px 16px;
  margin-right: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.btn-blue {
  background-color: #007bff;
  color: white;
}
.btn-red {
  background-color: #dc3545;
  color: white;
}
.btn-gray {
  background-color: #6c757d;
  color: white;
}
</style>