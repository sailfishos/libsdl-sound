Summary: Simple DirectMedia Layer - Sound File Decoding Library
Name: SDL2_sound
Version: 2.0.1
Release: 1
Source: %{name}-%{version}.tar.gz
URL: http://icculus.org/SDL_sound/
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
mkdir -p build
pushd build
%cmake \
       -DSDLSOUND_BUILD_STATIC:BOOL=OFF \
       ..
%make_build
popd

%install
pushd build
%make_install
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files playsound
%defattr(-,root,root)
%{_bindir}/*

%files devel
%defattr(-,root,root)
%doc docs/README.txt docs/CHANGELOG.txt docs/CREDITS.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h

