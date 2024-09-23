mapper_template_str = """
package {{ package_name }}.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import {{ package_name }}.entity.{{ entity_name }};
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface {{ class_name }} extends BaseMapper<{{ entity_name }}> {

}

"""
