<template>
    <div>
        <h1 class="m-10 text-center text-5xl">Más Vendidos</h1>
        <div class="mt-4 columns-3">
            <Libro />
            <Libro />
            <Libro />
        </div>
    </div>
</template>
<script>
import Libro from '../components/Libro.vue'
export default {
    components: {
        Libro
    }
}
</script>