<script lang="ts">
  import { onMount } from 'svelte';
  import { openUrl } from '@tauri-apps/plugin-opener';

  onMount(() => {
    const handler = (event: MouseEvent) => {
      const target = event.target as HTMLElement | null;
      if (!target) return;

      // find external links
      const anchor = target.closest<HTMLAnchorElement>('a[rel="external"]');
      if (!anchor) return;

      const href = anchor.getAttribute('href');
      if (!href) return;

      event.preventDefault();
      openUrl(href);
    };

    document.addEventListener('click', handler);
    return () => document.removeEventListener('click', handler);
  });
</script>

<h1 class="text-3xl font-bold underline">Welcome to SvelteKit</h1>
<p>
  Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation
</p>
