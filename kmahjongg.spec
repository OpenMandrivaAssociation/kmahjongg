Name:		kmahjongg
Summary:	A tile laying patience
Version:	15.12.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kmahjongg
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KDEGames)
BuildRequires:	kdelibs-devel
BuildRequires:	libkmahjongg4-devel
Requires:	libkdegames-common
Requires:	kmahjongglib

%description
In KMahjongg the tiles are scrambled and staked on top of each other to
resemble a certain shape. The player is then expected to remove all the
tiles off the game board by locating each tile's matching pair.

%files
%{_kde_bindir}/kmahjongg
%{_kde_applicationsdir}/kmahjongg.desktop
%{_kde_appsdir}/kmahjongg
%{_kde_docdir}/*/*/kmahjongg
%{_kde_iconsdir}/hicolor/*/apps/kmahjongg.*
%{_kde_datadir}/config.kcfg/kmahjongg.kcfg

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
