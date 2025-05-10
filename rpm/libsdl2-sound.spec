Summary: Simple DirectMedia Layer - Sound File Decoding Library
Name: SDL2_sound
Version: 2.0.4
Release: 1
Source: %{name}-%{version}.tar.gz
URL: https://github.com/sailfishos/libsdl-sound
License: zlib
BuildRequires: cmake
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(flac)

%description
SDL_sound is a library that handles the decoding of several popular sound file
formats, such as .WAV and .MP3. It is meant to make the programmer's sound
playback tasks simpler. The programmer gives SDL_sound a filename, or feeds it
data directly from one of many sources, and then reads the decoded waveform
data back at her leisure.

SDL_sound can also handle sample rate, audio format, and channel conversion
on-the-fly and behind-the-scenes, if the programmer desires.

%package playsound
Summary: Simple DirectMedia Layer - Sound File Decoding Library (playsound tool)
Requires: %{name}

%description playsound
SDL_sound is a library that handles the decoding of several popular sound file
formats, such as .WAV and .MP3. It is meant to make the programmer's sound
playback tasks simpler. The programmer gives SDL_sound a filename, or feeds it
data directly from one of many sources, and then reads the decoded waveform
data back at her leisure.

SDL_sound can also handle sample rate, audio format, and channel conversion
on-the-fly and behind-the-scenes, if the programmer desires.

This package contains the "playsound" utility.

%package devel
Summary: Simple DirectMedia Layer - Sound File Decoding Library (Development)
Requires: %{name}

%description devel
SDL_sound is a library that handles the decoding of several popular sound file
formats, such as .WAV and .MP3. It is meant to make the programmer's sound
playback tasks simpler. The programmer gives SDL_sound a filename, or feeds it
data directly from one of many sources, and then reads the decoded waveform
data back at her leisure.

SDL_sound can also handle sample rate, audio format, and channel conversion
on-the-fly and behind-the-scenes, if the programmer desires.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake -DSDLSOUND_BUILD_STATIC:BOOL=OFF
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files playsound
%{_bindir}/*

%files devel
%doc README.md docs/CHANGELOG.txt docs/CREDITS.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*.pc

