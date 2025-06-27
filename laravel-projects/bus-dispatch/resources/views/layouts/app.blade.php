<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel - {{ config('app.name') }}</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    <div class="min-h-screen bg-gray-100">
        <!-- Navigation -->
        <nav class="bg-blue-600 text-white shadow-md">
            <div class="container mx-auto px-4 py-3 flex justify-between items-center">
                <a href="{{ route('admin.dashboard') }}" class="text-xl font-bold">Admin Panel</a>
                <div class="flex items-center space-x-4">
                    <a href="{{ route('admin.users.index') }}" class="hover:underline">Users</a>
                    <form method="POST" action="{{ route('logout') }}">
                        @csrf
                        <button type="submit" class="hover:underline">Logout</button>
                    </form>
                </div>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="container mx-auto px-4 py-6">
            @yield('content')
        </main>
    </div>
</body>
</html>
