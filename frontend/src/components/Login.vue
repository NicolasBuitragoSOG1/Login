<template>
  <div>
    <div v-if="message" :class="['alert', messageType === 'success' ? 'alert-success' : 'alert-error']">
      {{ message }}
    </div>
    
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">Correo Electrónico</label>
        <input
          type="email"
          id="email"
          v-model="form.email"
          required
          placeholder="Ingresa tu correo"
        />
      </div>
      
      <div class="form-group">
        <label for="password">Contraseña</label>
        <input
          type="password"
          id="password"
          v-model="form.password"
          required
          placeholder="Ingresa tu contraseña"
        />
      </div>
      
      <button type="submit" class="btn" :disabled="loading">
        {{ loading ? 'Iniciando sesión...' : 'Iniciar Sesión' }}
      </button>
    </form>
    
    <div class="switch-form">
      ¿No tienes cuenta? <router-link to="/register">Regístrate aquí</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      loading: false,
      message: '',
      messageType: ''
    }
  },
  methods: {
    async handleLogin() {
      this.loading = true
      this.message = ''
      
      try {
        const response = await axios.post('/api/login', {
          email: this.form.email,
          password: this.form.password
        })
        
        this.message = 'Inicio de sesión exitoso'
        this.messageType = 'success'
        
        // Aquí podrías redirigir al usuario o guardar el token
        console.log('Login successful:', response.data)
        
      } catch (error) {
        this.message = error.response?.data?.detail || 'Error al iniciar sesión'
        this.messageType = 'error'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
