<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import { resolve } from '$app/paths';
  import ExternalLinkHandler from '$lib/ExternalLinkHandler.svelte';

  let { children } = $props();

  import '../app.css';
</script>

<ExternalLinkHandler />

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<div class="flex h-screen pr-1 bg-gray-700">
  <aside class="flex flex-col w-32 bg-gray-500 space-y-2 p-2">
    <nav>
      <ul>
        <li><a href={resolve('/')}>home</a></li>
        <li><a href={resolve('/text')}>texts</a></li>
        <li><a href="https://www.google.com" rel="external">external</a></li>
        <li>test3</li>
      </ul>
    </nav>
  </aside>
  <main class="flex-1 pl-3 bg-gray-700 overflow-auto custom-scrollbar">
    {@render children()}
  </main>
</div>
