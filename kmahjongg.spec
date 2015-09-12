Name:		kmahjongg
Summary:	A tile laying patience
Version:	15.04.3
Release:	3
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kmahjongg
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkmahjongg-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libkdegames4-devel
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
%cmake_kde4
%make

%install
%makeinstall_std -C build
