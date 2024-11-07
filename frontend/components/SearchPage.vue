<template>
    <div class="w-full flex justify-center items-start min-h-screen bg-gradient-to-r"
        :class="searchOptions.length ? 'from-gray-200 to-sky-300' : 'from-[#FCFCFCB2] to-cyan-50'"
    >
        <div class="w-full md:w-1/2 min-h-screen flex flex-col gap-5 p-6" >
            <div v-if="!loading" class="flex flex-col gap-5">
                <form 
                    @submit.prevent="submitQuery()"
                    class="flex justify-between relative"
                >
                    <input
                        v-model="query"
                        type="text" placeholder="Enter any message" 
                        class="w-full bg-transparent h-full outline-none text-lg border-b p-2"
                        @keyup.enter="submitQuery()"
                    >
                    <span @click="closeSearch" class="shadow-lg bg-transparent rounded-full absolute right-0">
                        <img src="~/assets/images/close.svg" alt="">
                    </span>
                </form>

                <Suggested v-if="searchOptions.length" title="This may be about" :options="searchOptions" :selectTopic />
                <TopChannels v-if="searchOptions.length" title="Suggested for" :selectedTopic="searchOptions[0]" :topChannels />
            </div>
            
            <div v-if="!loading && error" class="relative flex justify-center items-center flex-grow">
                <span class="absolute self-center w-1/2 text-center text-base" >{{ error }}</span>
                <img src="~/assets/images/loading.svg" alt="loading" class="w-full h-96" />
            </div>

            <div v-if="loading" class="flex justify-center items-center flex-grow animate-pulse">
                <img src="~/assets/images/loading.svg" alt="loading" class="w-full h-96" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    const emit = defineEmits(['toggleSearch'])
    const { loading, error, query, searchOptions, topChannels, submitQuery, selectTopic } = useTopics()

    const closeSearch = () => {
        query.value = ''
        searchOptions.value = []
        loading.value = false
        error.value = ''
        emit('toggleSearch')
    }
</script>

<style scoped>

</style>