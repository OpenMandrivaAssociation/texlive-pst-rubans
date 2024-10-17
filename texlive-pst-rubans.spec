Name:		texlive-pst-rubans
Version:	23464
Release:	2
Summary:	Draw three-dimensional ribbons
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-rubans
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-rubans.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-rubans.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-rubans.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses PStricks and pst-solides3d to draw three
dimensional ribbons on a cylinder, torus, sphere, cone or
paraboloid. The width of the ribbon, the number of turns, the
colour of the outer and the inner surface of the ribbon may be
set. In the case of circular and conical helices, one may also
choose the number of ribbons.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-rubans/pst-rubans.tex
%{_texmfdistdir}/tex/latex/pst-rubans/pst-rubans.sty
%doc %{_texmfdistdir}/doc/generic/pst-rubans/Changes
%doc %{_texmfdistdir}/doc/generic/pst-rubans/README
%doc %{_texmfdistdir}/doc/generic/pst-rubans/pst-rubans-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-rubans/pst-rubans-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-rubans/pst-rubans-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-rubans/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
