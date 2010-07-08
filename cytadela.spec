Summary:	A conversion of an Amiga Doom clone "Cytadela"
Summary(pl.UTF-8):	Konwersja amigowego klona gry Doom "Cytadela"
Name:		cytadela
Version:	1.0.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/cytadela/%{name}-%{version}.tar.bz2
# Source0-md5:	f9d47dc417ab306674074ac730c34032
Source1:	%{name}.desktop
URL:		http://sourceforge.net/projects/cytadela/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	vlc-devel >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cytadela is a conversion of an Amiga game also called Cytadela,
created by Virtual Design team. The conversion contains an
implementation of several algorithms taken from the original. Major
part of graphics, all music, sounds and levels are taken from the
original, but in some cases they are processed and/or modified in
order to make them easier to use with the conversion and to correct
some bugs.

%description -l pl.UTF-8
Cytadela jest konwersją amigowej gry o tym samym tytule, stworzonej
przez grupę Virtual Design. W konwersji wykorzystanych jest kilka
algorytmów pochodzących z oryginału. Cała muzyka, większość grafiki,
wszystkie dźwięki i poziomy pochodzą z wersji oryginalnej, ale w
niektórych przypadkach zostały przetworzone i/lub zmodyfikowane w celu
ułatwienia wykorzystania ich w konwersji i poprawienia kilku błędów.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/icons/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README data/doc/*.html
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
