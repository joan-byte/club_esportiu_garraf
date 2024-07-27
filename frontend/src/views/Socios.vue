<template>
  <div>
    <h1 class="text-3xl mb-4">Socios</h1>
    <div class="card mb-4">
      <h2 class="text-2xl mb-2">Crear Nuevo Socio</h2>
      <label for="socio-nombre" class="block">Nombre</label>
      <input id="socio-nombre" name="socio-nombre" v-model="nuevoSocio.nombre" placeholder="Nombre" class="input mb-2"/>
      <label for="socio-apellido" class="block">Apellido</label>
      <input id="socio-apellido" name="socio-apellido" v-model="nuevoSocio.apellido" placeholder="Apellido" class="input mb-2"/>
      <label for="socio-email" class="block">Email</label>
      <input id="socio-email" name="socio-email" v-model="nuevoSocio.email" placeholder="Email" class="input mb-2"/>
      <label for="socio-telefono" class="block">Teléfono</label>
      <input id="socio-telefono" name="socio-telefono" v-model="nuevoSocio.telefono" placeholder="Teléfono" class="input mb-2"/>
      <label for="socio-tipo_socio" class="block">Tipo de Socio</label>
      <input id="socio-tipo_socio" name="socio-tipo_socio" v-model="nuevoSocio.tipo_socio" placeholder="Tipo de Socio" class="input mb-2"/>
      <label for="socio-password" class="block">Contraseña</label>
      <input id="socio-password" name="socio-password" v-model="nuevoSocio.password" type="password" placeholder="Contraseña" class="input mb-2"/>
      <button @click="crearSocio" class="btn btn-blue">Crear</button>
    </div>
    <div v-for="socio in socios" :key="socio.id" class="card mb-4">
      <h2 class="text-2xl mb-2">{{ socio.nombre }} {{ socio.apellido }}</h2>
      <p>Email: {{ socio.email }}</p>
      <p>Teléfono: {{ socio.telefono }}</p>
      <p>Tipo de Socio: {{ socio.tipo_socio }}</p>
      <button @click="editarSocio(socio)" class="btn btn-blue">Modificar</button>
      <button @click="eliminarSocio(socio.id)" class="btn btn-red">Eliminar</button>
      <button @click="cancelarEdicion" class="btn btn-gray">Cancelar</button>
    </div>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'Socios',
  data() {
    return {
      socios: [],
      nuevoSocio: {
        nombre: '',
        apellido: '',
        email: '',
        telefono: '',
        tipo_socio: '',
        password: ''
      }
    }
  },
  mounted() {
    this.fetchSocios();
  },
  methods: {
    async fetchSocios() {
      try {
        const response = await api.getSocios();
        this.socios = response.data;
      } catch (error) {
        console.error("Error fetching socios:", error);
      }
    },
    async crearSocio() {
      try {
        await api.createSocio(this.nuevoSocio);
        this.fetchSocios();
        this.nuevoSocio = {
          nombre: '',
          apellido: '',
          email: '',
          telefono: '',
          tipo_socio: '',
          password: ''
        };
      } catch (error) {
        console.error("Error creating socio:", error);
      }
    },
    editarSocio(socio) {
      // Implementa la lógica para editar socio
    },
    async eliminarSocio(id) {
      try {
        await api.deleteSocio(id);
        this.fetchSocios();
      } catch (error) {
        console.error("Error deleting socio:", error);
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