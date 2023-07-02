// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "KevinSpel/KevinSpelGameModeBase.h"
#ifdef _MSC_VER
#pragma warning (push)
#pragma warning (disable : 4883)
#endif
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeKevinSpelGameModeBase() {}
// Cross Module References
	KEVINSPEL_API UClass* Z_Construct_UClass_AKevinSpelGameModeBase_NoRegister();
	KEVINSPEL_API UClass* Z_Construct_UClass_AKevinSpelGameModeBase();
	ENGINE_API UClass* Z_Construct_UClass_AGameModeBase();
	UPackage* Z_Construct_UPackage__Script_KevinSpel();
// End Cross Module References
	void AKevinSpelGameModeBase::StaticRegisterNativesAKevinSpelGameModeBase()
	{
	}
	UClass* Z_Construct_UClass_AKevinSpelGameModeBase_NoRegister()
	{
		return AKevinSpelGameModeBase::StaticClass();
	}
	struct Z_Construct_UClass_AKevinSpelGameModeBase_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UE4CodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_AKevinSpelGameModeBase_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_AGameModeBase,
		(UObject* (*)())Z_Construct_UPackage__Script_KevinSpel,
	};
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_AKevinSpelGameModeBase_Statics::Class_MetaDataParams[] = {
		{ "HideCategories", "Info Rendering MovementReplication Replication Actor Input Movement Collision Rendering Utilities|Transformation" },
		{ "IncludePath", "KevinSpelGameModeBase.h" },
		{ "ModuleRelativePath", "KevinSpelGameModeBase.h" },
		{ "ShowCategories", "Input|MouseInput Input|TouchInput" },
	};
#endif
	const FCppClassTypeInfoStatic Z_Construct_UClass_AKevinSpelGameModeBase_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<AKevinSpelGameModeBase>::IsAbstract,
	};
	const UE4CodeGen_Private::FClassParams Z_Construct_UClass_AKevinSpelGameModeBase_Statics::ClassParams = {
		&AKevinSpelGameModeBase::StaticClass,
		nullptr,
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		nullptr,
		nullptr,
		ARRAY_COUNT(DependentSingletons),
		0,
		0,
		0,
		0x009002A8u,
		METADATA_PARAMS(Z_Construct_UClass_AKevinSpelGameModeBase_Statics::Class_MetaDataParams, ARRAY_COUNT(Z_Construct_UClass_AKevinSpelGameModeBase_Statics::Class_MetaDataParams))
	};
	UClass* Z_Construct_UClass_AKevinSpelGameModeBase()
	{
		static UClass* OuterClass = nullptr;
		if (!OuterClass)
		{
			UE4CodeGen_Private::ConstructUClass(OuterClass, Z_Construct_UClass_AKevinSpelGameModeBase_Statics::ClassParams);
		}
		return OuterClass;
	}
	IMPLEMENT_CLASS(AKevinSpelGameModeBase, 3733062347);
	template<> KEVINSPEL_API UClass* StaticClass<AKevinSpelGameModeBase>()
	{
		return AKevinSpelGameModeBase::StaticClass();
	}
	static FCompiledInDefer Z_CompiledInDefer_UClass_AKevinSpelGameModeBase(Z_Construct_UClass_AKevinSpelGameModeBase, &AKevinSpelGameModeBase::StaticClass, TEXT("/Script/KevinSpel"), TEXT("AKevinSpelGameModeBase"), false, nullptr, nullptr, nullptr);
	DEFINE_VTABLE_PTR_HELPER_CTOR(AKevinSpelGameModeBase);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
#ifdef _MSC_VER
#pragma warning (pop)
#endif
