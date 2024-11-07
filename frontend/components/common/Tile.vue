<template>
    <div class="flex flex-col gap-1 px-4 py-2 bg-[#F4F4F4] rounded-2xl text-left">
        <!-- Topics -->
       <span class="text-base text-[#3A3A3A]">
        <slot name="topic"></slot>
       </span> 

        <!-- Mentions -->
       <span class="text-sm text-[#8F8F8F]">
        <slot name="mentions"></slot>
       </span> 
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>