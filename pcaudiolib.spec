%define major      0
%define libname    %mklibname pcaudio
%define devname %mklibname pcaudiolib -d

Name:           pcaudiolib
Version:        1.3
Release:        1
Summary:        Portable C Audio Library
Group:          System/Libraries
License:        GPLv3+
URL:            https://github.com/espeak-ng/pcaudiolib/
Source0:        https://github.com/espeak-ng/pcaudiolib/releases/download/%{version}/pcaudiolib-%{version}.tar.gz

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)

%description
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.

%package -n     %{libname}
Summary:        Portable C Audio Library
Group:          System/Libraries

%description -n %{libname}
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.


%package -n     %{devname}
Summary:        Development files for %{name}
Group:          Development/C++
Requires:       %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{devname}
Development files for the Portable C Audio Library.

#------------------------------------------------

%prep
%autosetup -p1

rm -rf src/TPCircularBuffer

%build
./autogen.sh
%configure --disable-static \
           --without-coreaudio
%make_build

%install
%make_install

%files -n %{libname}
%license COPYING
%doc AUTHORS ChangeLog.md README.md
%{_libdir}/libpcaudio.so.%{major}{,.*}

%files -n %{devname}
%{_libdir}/libpcaudio.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/audio.h
