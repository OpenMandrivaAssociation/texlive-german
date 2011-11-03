# revision 17039
# category Package
# catalog-ctan /language/german
# catalog-date 2009-09-26 12:32:55 +0200
# catalog-license lppl
# catalog-version 2.5e
Name:		texlive-german
Version:	2.5e
Release:	1
Summary:	Support for German typography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/german
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/german.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/german.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/german.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Supports the new German orthography (neue deutsche
Rechtschreibung).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/german/german.sty
%{_texmfdistdir}/tex/generic/german/ngerman.sty
%doc %{_texmfdistdir}/doc/generic/german/00readme.1st
%doc %{_texmfdistdir}/doc/generic/german/betatest/00readme.1st
%doc %{_texmfdistdir}/doc/generic/german/gerdoc.pdf
%doc %{_texmfdistdir}/doc/generic/german/gerdoc.tex
%doc %{_texmfdistdir}/doc/generic/german/german.MISSING
%doc %{_texmfdistdir}/doc/generic/german/hyphxmpl.cfg
#- source
%doc %{_texmfdistdir}/source/generic/german/german.dtx
%doc %{_texmfdistdir}/source/generic/german/german.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
