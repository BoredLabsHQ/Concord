<template>
    <div>
        <div 
            v-if="!isSearchOpen"  
            class="w-full min-h-screen flex justify-center items-start bg-gradient-to-br from-gray-200 to-sky-500"
        >
            <div class="w-full md:w-1/2 min-h-screen flex flex-col gap-5 p-6">
                <SearchBar @click="toggleSearch" />
                <Trending />
                <TopChannels title="Top channels for this topic" :selectedTopic :topChannels />
                <Suggested title="Suggested for you" :options="trending" :selectTopic />
            </div>
        </div>
        <SearchPage v-else @toggleSearch="toggleSearch" />
    </div>
</template>

<script setup lang="ts">
    const { trending, selectedTopic, topChannels, selectTopic} = useTopics()
    const isSearchOpen = ref(false)
    const toggleSearch = () => isSearchOpen.value = !isSearchOpen.value
</script>

<style scoped>

</style>