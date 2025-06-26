<?php

namespace App\Http\Controllers;

use App\Models\User;
use App\Models\Bus;
use App\Models\Trip;
use App\Models\Payment;
use Illuminate\Http\Request;


class AdminController extends Controller
{
    public function __construct()
    {
        $this->middleware('auth');
        $this->middleware('admin');
    }

    public function dashboard()
    {
        $stats = [
            'users' => User::count(),
            'buses' => Bus::count(),
            'trips' => Trip::where('status', '!=', 'cancelled')->count(),
            'revenue' => Payment::sum('amount'),
        ];

        return view('admin.dashboard', compact('stats'));
    }
}