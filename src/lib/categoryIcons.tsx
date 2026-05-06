import {
  LineChart, Building2, Shield, Trees, Bus, GraduationCap,
  Users, Home, BookOpen, FileText, Search,
  AlertCircle, Map, Sparkles, Database, BarChart3, PieChart,
  Calendar, Copy, Check, Moon, Sun, ChevronLeft, ChevronRight,
  ChevronsLeft, ChevronsRight, ArrowRight, X, Menu,
  Landmark, Heart, Vote, Stethoscope, Music, Briefcase, Activity,
} from 'lucide-react';
import type { ComponentType, SVGProps } from 'react';

export type IconComp = ComponentType<{ size?: number; className?: string } & SVGProps<SVGSVGElement>>;

// Mapa de slug-de-categoría (del API de Luján) o keys cortas → ícono
export const ICON_MAP: Record<string, IconComp> = {
  // Categorías Luján (slugs reales del portal)
  'gobierto-y-sector-publico': Landmark,
  'medio-ambiente-y-desarrollo-sustentable': Trees,
  'economia': LineChart,
  'urbanismo-y-territorio': Building2,
  'deporte-educacion-y-salud': GraduationCap,
  'honorable-consejo-deliberante-lujan-de-cuyo': Vote,
  'cultura-y-turismo': Music,
  'desarrollo-humano': Users,
  'movilidad': Bus,
  'elecciones': Vote,
  'genero': Heart,
  'gestion_de_datos': Database,
  'seguridad': Shield,
  'covid-19': Stethoscope,

  // Aliases / fallbacks
  gobierno: Landmark,
  ambiente: Trees,
  urbanismo: Building2,
  educacion: GraduationCap,
  deporte: Activity,
  hcd: Vote,
  cultura: Music,
  turismo: Music,
  desarrollo: Users,
  poblacion: Users,
  habitat: Home,
  fecundidad: Heart,
  industria: Briefcase,
  general: FileText,
  search: Search,
  error: AlertCircle,
};

export function getCategoryIcon(key: string): IconComp {
  if (!key) return FileText;
  const norm = key.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  return ICON_MAP[norm] ?? ICON_MAP[key] ?? FileText;
}

export {
  Sparkles, Database, BarChart3, PieChart, Calendar, Copy, Check,
  Moon, Sun, ChevronLeft, ChevronRight, ChevronsLeft, ChevronsRight,
  ArrowRight, X, Menu, Search, AlertCircle, Map, FileText,
};
