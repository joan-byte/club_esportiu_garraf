<template>
  <div>
    <h1 class="text-3xl mb-4">Pistas</h1>
    <div class="card mb-4">
      <h2 class="text-2xl mb-2">Crear Nueva Pista</h2>
      <label for="pista-nombre" class="block">Nombre</label>
      <input id="pista-nombre" name="pista-nombre" v-model="nuevaPista.nombre" placeholder="Nombre" class="input mb-2"/>
      <label for="pista-tipo_pista" class="block">Tipo de Pista</label>
      <input id="pista-tipo_pista" name="pista-tipo_pista" v-model="nuevaPista.tipo_pista" placeholder="Tipo de Pista" class="input mb-2"/>
      <label for="pista-tiempo_juego" class="block">Tiempo de Juego</label>
      <input id="pista-tiempo_juego" name="pista-tiempo_juego" v-model="nuevaPista.tiempo_juego" placeholder="Tiempo de Juego" class="input mb-2"/>
      <label for="pista-individuales" class="block">Individuales</label>
      <input id="pista-individuales" name="pista-individuales" type="checkbox" v-model="nuevaPista.individuales" class="input mb-2"/> Individuales
      <button @click="crearPista" class="btn btn-blue">Crear</button>
    </div>
    <div v-for="pista in pistas" :key="pista.id" class="card mb-4">
      <h2 class="text-2xl mb-2">{{ pista.nombre }}</h2>
      <p>Tipo: {{ pista.tipo_pista }}</p>
      <p>Tiempo de Juego: {{ pista.tiempo_juego }}</p>
      <p>Individuales: {{ pista.individuales ? 'Sí' : 'No' }}</p>
      <button @click="editarPista(pista)" class="btn btn-blue">Modificar</button>
      <button @click="eliminarPista(pista.id)" class="btn btn-red">Eliminar</button>
      <button @click="cancelarEdicion" class="btn btn-gray">Cancelar</button>
    </div>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'Pistas',
  data() {
    return {
      pistas: [],
      nuevaPista: {
        nombre: '',
        tipo_pista: '',
        tiempo_juego: '',
        individuales: false
      }
    }
  },
  mounted() {
    this.fetchPistas();
  },
  methods: {
    async fetchPistas() {
      try {
        const response = await api.getPistas();
        this.pistas = response.data;
      } catch (error) {
        console.error("Error fetching pistas:", error);
      }
    },
    async crearPista() {
      try {
        await api.createPista(this.nuevaPista);
        this.fetchPistas();
        this.nuevaPista = {
          nombre: '',
          tipo_pista: '',
          tiempo_juego: '',
          individuales: false
        };
      } catch (error) {
        console.error("Error creating pista:", error);
      }
    },
    editarPista(pista) {
      // Implementa la lógica para editar pista
    },
    async eliminarPista(id) {
      try {
        await api.deletePista(id);
        this.fetchPistas();
      } catch (error) {
        console.error("Error deleting pista:", error);
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