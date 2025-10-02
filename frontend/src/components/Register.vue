<template>
  <div>
    <div v-if="message" :class="['alert', messageType === 'success' ? 'alert-success' : 'alert-error']">
      {{ message }}
    </div>
    
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="name">Nombre Completo</label>
        <input
          type="text"
          id="name"
          v-model="form.name"
          required
          placeholder="Ingresa tu nombre completo"
        />
      </div>
      
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
          minlength="6"
        />
      </div>
      
      <div class="form-group">
        <label for="confirmPassword">Confirmar Contraseña</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="form.confirmPassword"
          required
          placeholder="Confirma tu contraseña"
        />
      </div>
      
      <button type="submit" class="btn" :disabled="loading">
        {{ loading ? 'Registrando...' : 'Registrarse' }}
      </button>
    </form>
    
    <div class="switch-form">
      ¿Ya tienes cuenta? <router-link to="/login">Inicia sesión aquí</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Register',
  data() {
    return {
      form: {
        name: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      loading: false,
      message: '',
      messageType: ''
    }
  },
  methods: {
    async handleRegister() {
      // Validar que las contraseñas coincidan
      if (this.form.password !== this.form.confirmPassword) {
        this.message = 'Las contraseñas no coinciden'
        this.messageType = 'error'
        return
      }
      
      this.loading = true
      this.message = ''
      
      try {
        const response = await axios.post('/api/register', {
          name: this.form.name,
          email: this.form.email,
          password: this.form.password
        })
        
        this.message = 'Registro exitoso. Ahora puedes iniciar sesión.'
        this.messageType = 'success'
        
        // Limpiar el formulario
        this.form = {
          name: '',
          email: '',
          password: '',
          confirmPassword: ''
        }
        
        console.log('Registration successful:', response.data)
        
      } catch (error) {
        this.message = error.response?.data?.detail || 'Error al registrar usuario'
        this.messageType = 'error'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
