<template>
    <Card>
        <div class="flex justify-between text-center">
            <span class="text-[#1C3B4F] font-bold text-[20px]">{{ $props.title }}</span>
            <img src="~/assets/images/star.svg" alt="Nature" />
        </div>
        <div class="flex flex-wrap justify-start items-center p-0">
            <span v-for="(topic,index) in props.options" :key="topic+index" class="text-native bg-white px-4 py-2 m-2 rounded-full"
                @click="selectTopic(topic)"
            >
                {{ topic }}
            </span>
        </div>
    </Card>
</template>
 
<script setup lang="ts">
    const props = defineProps(['title', 'options', 'selectTopic'])
</script>
 
<style scoped>
 
</style>