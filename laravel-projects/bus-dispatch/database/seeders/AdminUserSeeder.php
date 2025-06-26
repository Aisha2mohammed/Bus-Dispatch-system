<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class AdminUserSeeder extends Seeder
{
    public function run()
    {
        User::create([
            'username' => 'admin',
            'email' => 'admin@busdispatch.com',
            'password' => Hash::make('password'),
            'role' => 'admin',
            'status' => true,
        ]);

        $this->command->info('Admin user created successfully.');
    }
}
