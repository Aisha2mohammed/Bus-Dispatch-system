@extends('admin.layouts.app')

@section('content')
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
    <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-gray-500 text-sm font-medium">Total Users</h3>
        <p class="text-2xl font-bold">{{ $stats['users'] }}</p>
    </div>
    <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-gray-500 text-sm font-medium">Total Buses</h3>
        <p class="text-2xl font-bold">{{ $stats['buses'] }}</p>
    </div>
    <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-gray-500 text-sm font-medium">Total Trips</h3>
        <p class="text-2xl font-bold">{{ $stats['trips'] }}</p>
    </div>
    <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-gray-500 text-sm font-medium">Total Revenue</h3>
        <p class="text-2xl font-bold">${{ number_format($stats['revenue'], 2) }}</p>
    </div>
</div>

<div class="bg-white p-6 rounded-lg shadow">
    <h2 class="text-xl font-semibold mb-4">Recent Activities</h2>
    <p class="text-gray-500">No recent activities yet.</p>
</div>
@endsection