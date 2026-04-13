<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';

  let { children } = $props();

  import '../app.css';
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<div class="flex h-screen">
  <aside class="flex flex-col w-32 bg-gray-500 space-y-2 p-2">
    <div>Sidebar</div>
    <div>Test</div>
  </aside>
  <main class="flex-1 bg-gray-700 p-4 overflow-auto">
    {@render children()}
  </main>
</div>
