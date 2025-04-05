<script module>
    // ------ Icons -----
    import HomeIcon from 'lucide-svelte/icons/house';
    import TodoIcon from 'lucide-svelte/icons/list-todo';
    import NoteIcon from 'lucide-svelte/icons/notebook-pen';
    import UsersIcon from 'lucide-svelte/icons/users';
    // ------ Icons -----

    import { IsMobile } from '$lib';
    import { page } from '$app/state';
</script>

<script>
    const isMobile = new IsMobile();
</script>

<nav
    class="fixed bottom-2 left-[50%] -translate-x-[50%] p-2 w-full max-w-[400px]"
>
    <div class={[
        "w-full p-1 rounded-md",
        "bg-white not-dark:shadow-md not-dark:shadow-mint-700/10 text-mint-950",
        "dark:bg-mint-300"
    ]}
    >
        <ul class="grid grid-cols-4 gap-1">
            <li>
                <a href="/" class={[
                    "w-full text-sm text-mint-950 py-1 px-2 rounded-md flex flex-col gap-.5 items-center hover:bg-mint-700/10",
                    page.url.pathname === '/' && 'bg-mint-700/20'
                ]}>
                    <HomeIcon class="size-6" />
                    <span class="text-center whitespace-nowrap overflow-hidden text-ellipsis w-full max-w-[10ch]">Главная</span>
                </a>
            </li>
            <li>
                <a href="/todo" class={[
                    "w-full text-sm text-mint-950 py-1 px-2 rounded-md flex flex-col gap-.5 items-center hover:bg-mint-700/10",
                    page.url.pathname === '/todo' && 'bg-mint-700/20'
                ]}>
                    <TodoIcon class="size-6" />
                    <span class="text-center whitespace-nowrap overflow-hidden text-ellipsis w-full max-w-[10ch]">Задачи</span>
                </a>
            </li>
            <li>
                <a href="/note" class={[
                    "w-full text-sm text-mint-950 py-1 px-2 rounded-md flex flex-col gap-.5 items-center hover:bg-mint-700/10",
                    page.url.pathname === '/note' && 'bg-mint-700/20'
                ]}>
                    <NoteIcon class="size-6" />
                    <span class="text-center whitespace-nowrap overflow-hidden text-ellipsis w-full max-w-[10ch]">Заметки</span>
                </a>
            </li>
            <li>
                <a href="/users" class={[
                    "w-full text-sm text-mint-950 py-1 px-2 rounded-md flex flex-col gap-.5 items-center hover:bg-mint-700/10",
                    page.url.pathname === '/users' && 'bg-mint-700/20'
                ]}>
                    <UsersIcon class="size-6" />
                    <span class="text-center whitespace-nowrap overflow-hidden text-ellipsis w-full max-w-[10ch]">Пользователи</span>
                </a>
            </li>
        </ul>
    </div>
</nav>
