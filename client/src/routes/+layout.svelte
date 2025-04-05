<script module>
    import { Toaster } from 'svelte-sonner';
    import { ModeWatcher } from 'mode-watcher';
</script>

<script>
    import '../app.css';

	let { children } = $props();
</script>

{@render children()}
<ModeWatcher />
<Toaster />
