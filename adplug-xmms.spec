%define name adplug-xmms
%define version 1.2
%define release %mkrel 8

Summary: AdLib player plugin for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
Patch: adplug-xmms-1.2-missing-header.patch
URL: http://adplug.sourceforge.net/
License: LGPLv2+
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: xmms
BuildRequires: automake1.8
BuildRequires: libxmms-devel
BuildRequires: libadplug-devel >= 1.4 

%description
AdPlug/XMMS is an XMMS input plugin. XMMS is a cross-platform multimedia
player. AdPlug/XMMS uses the AdPlug AdLib sound player library to play back
a wide range of AdLib (OPL2) music file formats on top of an OPL2 emulator.
No OPL2 chip is required for playback.


%prep
%setup -q
%patch -p1
touch *
libtoolize --install --force
aclocal-1.8
autoconf
automake-1.8

%build
export CPPFLAGS="-I%_includedir/libbinio"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot/%_libdir/xmms/Input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO AUTHORS
%_libdir/xmms/Input/*so

