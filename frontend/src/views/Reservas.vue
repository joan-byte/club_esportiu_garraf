<template>
  <div>
    <h1 class="text-3xl">Reservas</h1>
    <ul>
      <li v-for="reserva in reservas" :key="reserva.id">
        Pista: {{ reserva.pista_id }}, Día: {{ reserva.dia }}, Hora: {{ reserva.hora_inicio }} - {{ reserva.hora_fin }}
      </li>
    </ul>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'Reservas',
  data() {
    return {
      reservas: []
    }
  },
  mounted() {
    this.fetchReservas();
  },
  methods: {
    async fetchReservas() {
      try {
        const response = await api.getReservas();
        this.reservas = response.data;
      } catch (error) {
        console.error("Error fetching reservas:", error);
      }
    }
  }
}
</script>